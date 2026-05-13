"use client";

import { useState } from "react";

import HeroSection from "@/components/HeroSection";
import TransactionForm from "@/components/TransactionForm";
import PredictionResults from "@/components/PredictionResults";
import PdfDownloadButton from "@/components/PdfDownloadButton";
import CsvUpload from "@/components/CsvUpload";
import BatchSummary from "@/components/BatchSummary";

import type {
  PredictionResponse,
  BatchResponse,
} from "@/lib/api";

export default function HomePage() {
  const [result, setResult] =
    useState<PredictionResponse | null>(null);

  const [transaction, setTransaction] =
    useState<Record<string, number> | null>(null);

  const [batchResult, setBatchResult] =
    useState<BatchResponse | null>(null);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <HeroSection />

      {/* Single Transaction Analysis */}
      <section
        id="analyzer"
        className="border-b border-slate-800 px-6 py-20"
      >
        <div className="mx-auto max-w-7xl space-y-8">
          <TransactionForm
            onResult={(prediction, tx) => {
              setResult(prediction);
              setTransaction(tx);
            }}
          />

          {result && transaction && (
            <div className="space-y-6">
              <PredictionResults result={result} />
              <PdfDownloadButton
                transaction={transaction}
              />
            </div>
          )}
        </div>
      </section>

      {/* Batch CSV Analysis */}
      <section className="px-6 py-20">
        <div className="mx-auto max-w-7xl space-y-8">
          <CsvUpload onResult={setBatchResult} />

          {batchResult && (
            <BatchSummary result={batchResult} />
          )}
        </div>
      </section>
    </main>
  );
}