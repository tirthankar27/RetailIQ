"use client";

import Link from "next/link";
import { LayoutDashboard, Upload, BarChart3, FileText } from "lucide-react";

export default function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 flex h-screen w-72 flex-col border-r border-slate-200 bg-white">
      <div className="border-b border-slate-200 p-8">
        <div className="flex items-center gap-3">
          <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-600 to-indigo-600 text-xl text-white">
            🛍
          </div>

          <div>
            <h1 className="text-2xl font-extrabold tracking-tight text-slate-900">
              RetailIQ
            </h1>

            <p className="text-sm text-slate-500">Retail Analytics Platform</p>
          </div>
        </div>
      </div>

      <nav className="flex-1 p-5">
        <p className="mb-3 px-3 text-xs font-semibold uppercase tracking-wider text-slate-400">
          Navigation
        </p>

        <div className="space-y-2">
          <Link
            href="/"
            className="
              flex
              items-center
              gap-3
              rounded-xl
              bg-blue-50
              px-4
              py-3
              font-medium
              text-blue-700
              transition-all
              hover:bg-blue-100
            "
          >
            <LayoutDashboard size={18} />
            Dashboard
          </Link>

          <Link
            href="/upload"
            className="
              flex
              items-center
              gap-3
              rounded-xl
              px-4
              py-3
              text-slate-700
              transition-all
              hover:bg-slate-100
            "
          >
            <Upload size={18} />
            Upload Dataset
          </Link>

          <Link
            href="#"
            className="
              flex
              items-center
              gap-3
              rounded-xl
              px-4
              py-3
              text-slate-700
              transition-all
              hover:bg-slate-100
            "
          >
            <BarChart3 size={18} />
            Analytics
          </Link>

          <Link
            href="#"
            className="
              flex
              items-center
              gap-3
              rounded-xl
              px-4
              py-3
              text-slate-700
              transition-all
              hover:bg-slate-100
            "
          >
            <FileText size={18} />
            Reports
          </Link>
        </div>
      </nav>

      <div className="border-t border-slate-200 p-5">
        <div className="rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 p-4 text-white">
          <p className="text-sm font-medium">RetailIQ</p>

          <p className="mt-1 text-xs text-blue-100">
            AI-powered retail intelligence and reporting platform.
          </p>
        </div>
      </div>
    </aside>
  );
}
