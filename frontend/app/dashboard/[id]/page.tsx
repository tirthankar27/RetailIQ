"use client";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { api } from "@/lib/api";
import KPICard from "@/components/dashboard/KPICard";
import DashboardLayout from "@/components/layout/DashboardLayout";
import RevenueChart from "@/components/dashboard/RevenueChart";
import SegmentChart from "@/components/dashboard/SegmentChart";
import TopCustomers from "@/components/dashboard/TopCustomers";
import TopProducts from "@/components/dashboard/TopProducts";
import Insights from "@/components/dashboard/Insights";
import ChurnChart from "@/components/dashboard/ChurnChart";

type HighRiskCustomer = {
  customer_id: number;
  churn_probability: number;
};

type Prediction = {
  total_customers: number;
  predicted_churners: number;
  predicted_active: number;
  churn_rate: number;
  high_risk_customers: HighRiskCustomer[];
};

type Dashboard = {
  kpis: {
    revenue: number;
    orders: number;
    customers: number;
    average_order_value: number;
  };
  rfm_summary: {
    total_customers: number;
    average_recency: number;
    average_frequency: number;
    average_monetary: number;
  };
  segments: Record<string, number>;
};

type Revenue = {
  Month: string;
  Revenue: number;
};

type Segment = {
  name: string;
  value: number;
};

type Customer = {
  CustomerID: number;
  Revenue: number;
};

type Product = {
  Product: string;
  Revenue: number;
};

export default function DashboardPage() {
  const params = useParams();
  const router = useRouter();

  const [dashboard, setDashboard] = useState<Dashboard | null>(null);
  const [revenue, setRevenue] = useState<Revenue[]>([]);
  const [segments, setSegments] = useState<Segment[]>([]);
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [products, setProducts] = useState<Product[]>([]);
  const [prediction, setPrediction] = useState<Prediction | null>(null);
  const [insights, setInsights] = useState<string[]>([]);

  useEffect(() => {
    const loadData = async () => {
      const [
        dashboardRes,
        revenueRes,
        segmentRes,
        customerRes,
        productRes,
        insightsRes,
        predictionRes,
      ] = await Promise.all([
        api.get(`/dashboard/${params.id}`),
        api.get(`/revenue/${params.id}`),
        api.get(`/segments/${params.id}`),
        api.get(`/customers/top/${params.id}`),
        api.get(`/products/top/${params.id}`),
        api.get(`/insights/${params.id}`),
        api.get(`/predict/${params.id}`),
      ]);

      setDashboard(dashboardRes.data);
      setRevenue(revenueRes.data);

      setSegments(
        Object.entries(segmentRes.data.segments).map(([name, value]) => ({
          name,
          value: Number(value),
        })),
      );

      setCustomers(customerRes.data);
      setProducts(productRes.data);
      setInsights(insightsRes.data.insights);
      setPrediction(predictionRes.data);
    };

    void loadData();
  }, [params.id]);

  function downloadReport() {
    window.open(`http://localhost:8000/api/report/${params.id}`, "_blank");
  }

  if (!dashboard) {
    return (
      <div className="flex h-screen items-center justify-center">
        <div className="text-lg text-slate-500">Loading dashboard...</div>
      </div>
    );
  }

  return (
    <DashboardLayout>
      <div className="mx-auto max-w-7xl p-8">
        <div className="mb-8 rounded-3xl bg-gradient-to-r from-blue-600 to-indigo-600 p-8 text-white">
          <p className="text-blue-100">Welcome back 👋</p>

          <h1 className="mt-2 text-4xl font-bold">
            Retail Performance Overview
          </h1>

          <p className="mt-2 text-blue-100">
            AI-powered retail intelligence dashboard
          </p>
          <div className="mt-6 flex gap-3">
            <button
              onClick={downloadReport}
              className="rounded-xl bg-white px-5 py-3 font-medium text-blue-700"
            >
              Download Report
            </button>

            <button
              onClick={() => router.push("/upload")}
              className="rounded-xl border border-white/30 px-5 py-3 font-medium text-white"
            >
              Upload Dataset
            </button>
          </div>
        </div>

        <div className="mb-8 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          <KPICard title="Revenue" value={dashboard.kpis.revenue} />
          <KPICard title="Orders" value={dashboard.kpis.orders} />
          <KPICard title="Customers" value={dashboard.kpis.customers} />
          <KPICard title="AOV" value={dashboard.kpis.average_order_value} />
          <KPICard
            title="Predicted Churners"
            value={prediction?.predicted_churners ?? 0}
          />
          <KPICard
            title="Churn Rate"
            value={`${prediction?.churn_rate ?? 0}%`}
          />
        </div>

        <ChurnChart
          active={prediction?.predicted_active ?? 0}
          churners={prediction?.predicted_churners ?? 0}
        />

        <div className="grid gap-6 lg:grid-cols-2">
          <RevenueChart data={revenue} />
          <SegmentChart data={segments} />
        </div>
        <div className="mt-6 grid gap-6 lg:grid-cols-2">
          <TopCustomers data={customers} />

          <TopProducts data={products} />
        </div>
        <div className="mt-6">
          <Insights insights={insights} />
        </div>
        {prediction && (
          <div className="mt-6 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
            <h2 className="mb-4 text-xl font-semibold">
              Top Customers Likely To Churn
            </h2>

            <table className="w-full">
              <thead>
                <tr className="border-b">
                  <th className="py-2 text-left">Customer ID</th>

                  <th className="py-2 text-left">Churn Probability</th>
                </tr>
              </thead>

              <tbody>
                {prediction.high_risk_customers?.map(
                  (customer: HighRiskCustomer) => (
                    <tr key={customer.customer_id} className="border-b">
                      <td className="py-2">{customer.customer_id}</td>

                      <td className="py-2">{customer.churn_probability}%</td>
                    </tr>
                  ),
                )}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </DashboardLayout>
  );
}
