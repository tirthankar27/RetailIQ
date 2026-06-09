type Props = {
  title: string;
  value: string | number;
};

export default function KPICard({ title, value }: Props) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all hover:shadow-md">
      <p className="text-sm font-medium text-slate-500">{title}</p>

      <h3 className="mt-3 text-4xl font-bold text-slate-900">
        {typeof value === "number"
          ? value.toLocaleString(undefined, {
              maximumFractionDigits: 2,
            })
          : value}
      </h3>
    </div>
  );
}
