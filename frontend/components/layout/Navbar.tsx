import {
  Upload,
  Download,
} from "lucide-react";

export default function Navbar() {
  return (
    <div
      className="
        mb-6
        rounded-2xl
        border
        border-slate-200
        bg-white
        p-6
        shadow-sm
      "
    >
      <div className="flex items-center justify-between">

        <div>

          <div className="flex items-center gap-3">

            <div
              className="
                flex
                h-12
                w-12
                items-center
                justify-center
                rounded-xl
                bg-blue-100
                text-xl
              "
            >
              📊
            </div>

            <div>

              <p className="text-sm font-medium text-blue-600">
                RetailIQ Analytics
              </p>

              <h1 className="text-2xl font-bold text-slate-900">
                Retail Performance Overview
              </h1>

            </div>

          </div>

          <div className="mt-4 flex gap-4 text-sm">

            <span className="rounded-full bg-blue-50 px-3 py-1 text-blue-700">
              Revenue Analytics
            </span>

            <span className="rounded-full bg-emerald-50 px-3 py-1 text-emerald-700">
              Customer Intelligence
            </span>

            <span className="rounded-full bg-purple-50 px-3 py-1 text-purple-700">
              AI Insights
            </span>

          </div>

        </div>

        <div className="flex items-center gap-3">

          <button
            className="
              flex
              items-center
              gap-2
              rounded-xl
              border
              border-slate-200
              bg-white
              px-4
              py-2.5
              font-medium
              text-slate-700
              transition-all
              hover:bg-slate-50
            "
          >
            <Upload size={16} />
            Upload Dataset
          </button>

          <button
            className="
              flex
              items-center
              gap-2
              rounded-xl
              bg-blue-600
              px-4
              py-2.5
              font-medium
              text-white
              shadow-sm
              transition-all
              hover:bg-blue-700
            "
          >
            <Download size={16} />
            Download Report
          </button>

        </div>

      </div>
    </div>
  );
}