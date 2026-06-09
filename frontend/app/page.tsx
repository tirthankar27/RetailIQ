import Link from "next/link";
import Navbar from "@/components/layout/Navbar";

export default function HomePage() {
  return (
    <>
      <Navbar />

      <main className="mx-auto max-w-5xl px-6 py-24">

        <h1 className="text-5xl font-bold tracking-tight">
          Retail Analytics
          for Any Dataset
        </h1>

        <p className="mt-6 max-w-2xl text-lg text-slate-600">
          Upload CSV or Excel files,
          automatically detect schema,
          and generate customer analytics,
          segmentation and insights.
        </p>

        <Link
          href="/upload"
          className="mt-10 inline-flex rounded-lg bg-black px-5 py-3 text-white"
        >
          Get Started
        </Link>

      </main>
    </>
  );
}