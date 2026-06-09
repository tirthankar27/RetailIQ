export default function Insights({ insights }: { insights: string[] }) {
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
        <h2 className="text-xl font-semibold text-slate-900">AI Insights</h2>

        <p className="mt-1 text-sm text-slate-500">
          Automatically generated business observations
        </p>
      </div>

      <div className="space-y-4">
        {insights.map((insight, index) => (
          <div
            key={index}
            className="
                flex
                items-start
                gap-4
                rounded-xl
                border
                border-blue-100
                bg-blue-50
                p-4
              "
          >
            <div
              className="
                  flex
                  h-10
                  w-10
                  items-center
                  justify-center
                  rounded-full
                  bg-blue-600
                  text-white
                "
            >
              💡
            </div>

            <p className="text-slate-700">{insight}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
