import Navbar from "@/components/layout/Navbar";
import FileUploader from "@/components/upload/FileUploader";

export default function UploadPage() {
  return (
    <>
      <Navbar />

      <main className="mx-auto max-w-4xl px-6 py-12">

        <h2 className="mb-6 text-3xl font-semibold">
          Upload Dataset
        </h2>

        <FileUploader />

      </main>
    </>
  );
}