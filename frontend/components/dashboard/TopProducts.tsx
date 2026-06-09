type Product = {
  Product: string;
  Revenue: number;
};

export default function TopProducts({ data }: { data: Product[] }) {
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
        <h2 className="text-xl font-semibold text-slate-900">Top Products</h2>

        <p className="mt-1 text-sm text-slate-500">
          Highest revenue generating products
        </p>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr className="border-b border-slate-200">
              <th className="pb-4 text-left text-xs font-semibold uppercase tracking-wider text-slate-500">
                Product
              </th>

              <th className="pb-4 text-right text-xs font-semibold uppercase tracking-wider text-slate-500">
                Revenue
              </th>
            </tr>
          </thead>

          <tbody>
            {data.map((product, index) => (
              <tr
                key={index}
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
                        bg-emerald-100
                        text-sm
                        font-semibold
                        text-emerald-700
                      "
                    >
                      #{index + 1}
                    </div>

                    <span className="font-medium text-slate-800">
                      {product.Product}
                    </span>
                  </div>
                </td>

                <td className="py-4 text-right font-semibold text-slate-900">
                  ₹{" "}
                  {product.Revenue.toLocaleString(undefined, {
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
