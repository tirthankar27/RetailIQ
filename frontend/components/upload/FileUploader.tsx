"use client";

import { useState } from "react";
import { UploadCloud } from "lucide-react";
import { useRouter } from "next/navigation";
import { api } from "@/lib/api";

export default function FileUploader() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const router = useRouter();

  async function handleUpload() {
    if (!file) return;

    try {
      setLoading(true);

      const formData = new FormData();

      formData.append("file", file);

      const response = await api.post("/upload/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      router.push(`/analyze/${response.data.id}`);
    } catch (error) {
      console.error(error);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      className="
        rounded-3xl
        border
        border-slate-200
        bg-white
        p-10
        shadow-sm
      "
    >
      <div className="text-center">
        <div
          className="
            mx-auto
            flex
            h-20
            w-20
            items-center
            justify-center
            rounded-3xl
            bg-gradient-to-br
            from-blue-600
            to-indigo-600
            text-white
          "
        >
          <UploadCloud size={40} />
        </div>

        <h2 className="mt-6 text-3xl font-bold text-slate-900">
          Upload Your Dataset
        </h2>

        <p className="mt-3 text-slate-500">
          Upload CSV or Excel files and generate instant customer insights.
        </p>
      </div>

      <div className="mt-10">
        <label
          className="
            flex
            cursor-pointer
            flex-col
            items-center
            justify-center
            rounded-2xl
            border-2
            border-dashed
            border-slate-300
            p-10
            transition-all
            hover:border-blue-500
            hover:bg-blue-50
          "
        >
          <input
            type="file"
            accept=".csv,.xls,.xlsx"
            className="hidden"
            onChange={(e) => {
              if (e.target.files?.[0]) {
                setFile(e.target.files[0]);
              }
            }}
          />

          <UploadCloud size={36} className="text-slate-400" />

          <p className="mt-4 font-medium text-slate-700">
            Click to select a file
          </p>

          <p className="mt-1 text-sm text-slate-500">CSV, XLS or XLSX</p>
        </label>
      </div>

      {file && (
        <div
          className="
            mt-6
            rounded-xl
            bg-slate-50
            p-4
          "
        >
          <p className="text-sm font-medium text-slate-700">Selected File</p>

          <p className="mt-1 text-slate-600">{file.name}</p>
        </div>
      )}

      <button
        onClick={handleUpload}
        disabled={!file || loading}
        className="
          mt-8
          w-full
          rounded-2xl
          bg-gradient-to-r
          from-blue-600
          to-indigo-600
          px-6
          py-4
          font-semibold
          text-white
          transition-all
          hover:scale-[1.01]
          hover:shadow-lg
          disabled:cursor-not-allowed
          disabled:opacity-50
        "
      >
        {loading ? "Uploading..." : "Upload & Analyze"}
      </button>
    </div>
  );
}
