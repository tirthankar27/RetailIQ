"use client";

import { useRouter, useParams } from "next/navigation";
import { useEffect, useState } from "react";
import { api } from "@/lib/api";

export default function AnalyzePage() {
  const params = useParams();
  const router = useRouter();

  const [data, setData] = useState<any>(null);

  const [mapping, setMapping] = useState({
    customer_column: "",
    date_column: "",
    quantity_column: "",
    price_column: "",
    product_column: "",
  });

  useEffect(() => {
    fetchData();
  }, []);

  async function fetchData() {
    try {
      const response = await api.get(`/analyze/${params.id}`);

      setData(response.data);

      const suggested = response.data.suggested_mapping;

      setMapping({
        customer_column: suggested.customer || "",

        date_column: suggested.date || "",

        quantity_column: suggested.quantity || "",

        price_column: suggested.price || "",

        product_column: suggested.product || "",
      });
    } catch (error) {
      console.error(error);
    }
  }

  async function saveMapping() {
    try {
      await api.post(`/mapping/${params.id}`, mapping);

      router.push(`/dashboard/${params.id}`);
    } catch (error) {
      console.error(error);
      alert("Failed to save mapping");
    }
  }

  if (!data) {
    return (
      <div className="flex h-screen items-center justify-center">
        <div className="text-lg text-slate-500">Loading dataset...</div>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-7xl p-8">
      <div className="mb-8">
        <p className="text-sm font-medium text-blue-600">RetailIQ Analytics</p>

        <h1 className="mt-1 text-4xl font-bold text-slate-900">
          Dataset Analysis
        </h1>

        <p className="mt-2 text-slate-500">
          Review detected columns and confirm the mapping before generating
          insights.
        </p>
      </div>

      <div
        className="
          mb-6
          rounded-2xl
          border
          border-emerald-200
          bg-emerald-50
          p-5
        "
      >
        <p className="font-semibold text-emerald-700">
          ✓ Dataset detected successfully
        </p>

        <p className="mt-1 text-sm text-emerald-600">
          {data.columns.length} columns detected • {data.preview.length} preview
          rows loaded
        </p>
      </div>

      <div className="grid gap-6 lg:grid-cols-12">
        <div className="lg:col-span-4">
          <div
            className="
    h-[650px]
    rounded-2xl
    border
    border-slate-200
    bg-white
    p-6
    shadow-sm
  "
          >
            <h2 className="mb-6 text-xl font-semibold text-slate-900">
              Column Mapping
            </h2>

            <div className="space-y-4">
              <MappingSelect
                label="Customer"
                value={mapping.customer_column}
                columns={data.columns}
                onChange={(value) =>
                  setMapping({
                    ...mapping,
                    customer_column: value,
                  })
                }
              />

              <MappingSelect
                label="Date"
                value={mapping.date_column}
                columns={data.columns}
                onChange={(value) =>
                  setMapping({
                    ...mapping,
                    date_column: value,
                  })
                }
              />

              <MappingSelect
                label="Quantity"
                value={mapping.quantity_column}
                columns={data.columns}
                onChange={(value) =>
                  setMapping({
                    ...mapping,
                    quantity_column: value,
                  })
                }
              />

              <MappingSelect
                label="Price"
                value={mapping.price_column}
                columns={data.columns}
                onChange={(value) =>
                  setMapping({
                    ...mapping,
                    price_column: value,
                  })
                }
              />

              <MappingSelect
                label="Product"
                value={mapping.product_column}
                columns={data.columns}
                onChange={(value) =>
                  setMapping({
                    ...mapping,
                    product_column: value,
                  })
                }
              />

              <button
                onClick={saveMapping}
                className="
                  mt-4
                  w-full
                  rounded-xl
                  bg-blue-600
                  px-6
                  py-4
                  font-semibold
                  text-white
                  transition-all
                  hover:bg-blue-700
                "
              >
                Continue to Dashboard →
              </button>
            </div>
          </div>
        </div>

        <div className="lg:col-span-8">
          <div
            className="
    h-[650px]
    rounded-2xl
    border
    border-slate-200
    bg-white
    p-6
    shadow-sm
  "
          >
            <h2 className="mb-4 text-xl font-semibold text-slate-900">
              Data Preview
            </h2>

            <div
              className="
    h-[560px]
    overflow-auto
    rounded-xl
    border
    border-slate-100
  "
            >
              <table className="min-w-full">
                <thead>
                  <tr>
                    {data.columns.map((column: string) => (
                      <th
                        key={column}
                        className="
    sticky
    top-0
    z-10
    border-b
    bg-slate-50
    px-4
    py-3
    text-left
    text-sm
    font-semibold
    text-slate-700
  "
                      >
                        {column}
                      </th>
                    ))}
                  </tr>
                </thead>

                <tbody>
                  {data.preview.map((row: any, index: number) => (
                    <tr key={index} className="hover:bg-slate-50">
                      {data.columns.map((column: string) => (
                        <td
                          key={column}
                          className="
                                border-b
                                px-4
                                py-3
                                text-sm
                                text-slate-700
                              "
                        >
                          {String(row[column])}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function MappingSelect({
  label,
  value,
  columns,
  onChange,
}: {
  label: string;
  value: string;
  columns: string[];
  onChange: (value: string) => void;
}) {
  return (
    <div>
      <label className="mb-2 block text-sm font-medium text-slate-700">
        {label}
      </label>

      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="
          w-full
          rounded-xl
          border
          border-slate-200
          bg-white
          px-4
          py-3
          shadow-sm
          focus:border-blue-500
          focus:outline-none
        "
      >
        <option value="">Select Column</option>

        {columns.map((column) => (
          <option key={column} value={column}>
            {column}
          </option>
        ))}
      </select>
    </div>
  );
}
