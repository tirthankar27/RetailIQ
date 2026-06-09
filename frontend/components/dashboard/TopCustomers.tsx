type Customer = {
  CustomerID: number;
  Revenue: number;
};

export default function TopCustomers({ data }: { data: Customer[] }) {
  return (
    <div
      className="
        rounded-2xl
        border
        border-slate-200
        bg-white
        p-6
        shadow-sm
      "
    >
      <div className="mb-6">
        <h2 className="text-xl font-semibold text-slate-900">Top Customers</h2>

        <p className="mt-1 text-sm text-slate-500">
          Highest revenue generating customers
        </p>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr className="border-b border-slate-200">
              <th className="pb-4 text-left text-xs font-semibold uppercase tracking-wider text-slate-500">
                Customer
              </th>

              <th className="pb-4 text-right text-xs font-semibold uppercase tracking-wider text-slate-500">
                Revenue
              </th>
            </tr>
          </thead>

          <tbody>
            {data.map((customer, index) => (
              <tr
                key={customer.CustomerID}
                className="
                  border-b
                  border-slate-100
                  transition-colors
                  hover:bg-slate-50
                "
              >
                <td className="py-4">
                  <div className="flex items-center gap-3">
                    <div
                      className="
                        flex
                        h-8
                        w-8
                        items-center
                        justify-center
                        rounded-full
                        bg-blue-100
                        text-sm
                        font-semibold
                        text-blue-700
                      "
                    >
                      #{index + 1}
                    </div>

                    <span className="font-medium text-slate-800">
                      {customer.CustomerID}
                    </span>
                  </div>
                </td>

                <td className="py-4 text-right font-semibold text-slate-900">
                  ₹{" "}
                  {customer.Revenue.toLocaleString(undefined, {
                    maximumFractionDigits: 2,
                  })}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
