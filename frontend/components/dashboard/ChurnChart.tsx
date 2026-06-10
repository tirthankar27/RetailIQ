"use client";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function ChurnChart({
  active,
  churners,
}: {
  active: number;
  churners: number;
}) {

  const data = [
    {
      name: "Active",
      value: active,
    },

    {
      name: "Churn Risk",
      value: churners,
    },
  ];

  return (
    <div className="rounded-2xl bg-white p-6 shadow">
      <h2 className="mb-4 text-xl font-semibold">
        Customer Risk Distribution
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            outerRadius={100}
          >
            <Cell fill="#10B981" />
            <Cell fill="#EF4444" />
          </Pie>

          <Tooltip />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}