"use client";

import { downloadPdf } from "@/lib/api";

interface PdfDownloadButtonProps {
  transaction: Record<string, number>;
}

export default function PdfDownloadButton({
  transaction,
}: PdfDownloadButtonProps) {
  async function handleDownload() {
    try {
      const blob = await downloadPdf(transaction);

      const url = window.URL.createObjectURL(blob);

      const link = document.createElement("a");
      link.href = url;
      link.download = "fraud_report.pdf";

      document.body.appendChild(link);
      link.click();
      link.remove();

      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error("PDF download failed:", error);
      alert("Failed to generate PDF report.");
    }
  }

  return (
    <button
      onClick={handleDownload}
      className="w-full rounded-2xl bg-indigo-600 px-6 py-4 font-semibold text-white transition hover:bg-indigo-500"
    >
      Download Investigation Report (PDF)
    </button>
  );
}