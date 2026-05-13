"use client";

import { useState } from "react";
import { uploadCsv, BatchResponse } from "@/lib/api";

interface CsvUploadProps {
  onResult: (result: BatchResponse) => void;
}

export default function CsvUpload({
  onResult,
}: CsvUploadProps) {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleUpload() {
    if (!file) {
      setError("Please select a CSV file.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const result = await uploadCsv(file);
      onResult(result);
    } catch (err) {
      console.error(err);
      setError("Failed to analyze CSV file.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="rounded-3xl border border-slate-800 bg-slate-900 p-8">
      <div className="mb-6">
        <h2 className="text-3xl font-bold">
          Batch CSV Analysis
        </h2>
        <p className="mt-2 text-slate-400">
          Upload a CSV file containing thousands of transactions.
        </p>
      </div>

      <input
        type="file"
        accept=".csv"
        onChange={(e) =>
          setFile(e.target.files?.[0] || null)
        }
        className="mb-4 block w-full rounded-xl border border-slate-700 bg-slate-950 p-3 text-sm"
      />

      {file && (
        <p className="mb-4 text-sm text-slate-400">
          Selected: {file.name}
        </p>
      )}

      <button
        onClick={handleUpload}
        disabled={loading}
        className="w-full rounded-2xl bg-white px-6 py-4 font-semibold text-slate-900 transition hover:bg-slate-200 disabled:opacity-50"
      >
        {loading ? "Analyzing CSV..." : "Analyze CSV File"}
      </button>

      {error && (
        <p className="mt-4 text-sm text-red-400">
          {error}
        </p>
      )}
    </div>
  );
}