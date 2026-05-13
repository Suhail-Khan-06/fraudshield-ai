"use client";

import { useState } from "react";
import { predictTransaction, PredictionResponse } from "@/lib/api";

interface TransactionFormProps {
  onResult: (result: PredictionResponse, transaction: Record<string, number>) => void;
}

function getSampleTransaction(): Record<string, number> {
  return {
    Time: 0,
    V1: -1.359807,
    V2: -0.072781,
    V3: 2.536347,
    V4: 1.378155,
    V5: -0.338321,
    V6: 0.462388,
    V7: 0.239599,
    V8: 0.098698,
    V9: 0.363787,
    V10: 0.090794,
    V11: -0.5516,
    V12: -0.617801,
    V13: -0.99139,
    V14: -0.311169,
    V15: 1.468177,
    V16: -0.470401,
    V17: 0.207971,
    V18: 0.025791,
    V19: 0.403993,
    V20: 0.251412,
    V21: -0.018307,
    V22: 0.277838,
    V23: -0.110474,
    V24: 0.066928,
    V25: 0.128539,
    V26: -0.189115,
    V27: 0.133558,
    V28: -0.021053,
    Amount: 149.62,
  };
}

export default function TransactionForm({
  onResult,
}: TransactionFormProps) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [transaction] = useState<Record<string, number>>(
    getSampleTransaction()
  );

  async function handleAnalyze() {
    try {
      setLoading(true);
      setError("");

      const result = await predictTransaction(transaction);
      onResult(result, transaction);
    } catch (err) {
      console.error(err);
      setError("Failed to analyze transaction.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="rounded-3xl border border-slate-800 bg-slate-900 p-8">
      <div className="mb-6">
        <h2 className="text-3xl font-bold">Transaction Analyzer</h2>
        <p className="mt-2 text-slate-400">
          Analyze a preloaded sample transaction using your fraud
          detection models.
        </p>
      </div>

      <div className="mb-6 grid gap-4 md:grid-cols-2">
        <div className="rounded-2xl bg-slate-950 p-4">
          <div className="text-sm text-slate-400">Amount</div>
          <div className="mt-1 text-2xl font-bold">
            ${transaction.Amount}
          </div>
        </div>

        <div className="rounded-2xl bg-slate-950 p-4">
          <div className="text-sm text-slate-400">Time</div>
          <div className="mt-1 text-2xl font-bold">
            {transaction.Time}
          </div>
        </div>
      </div>

      <button
        onClick={handleAnalyze}
        disabled={loading}
        className="w-full rounded-2xl bg-white px-6 py-4 font-semibold text-slate-900 transition hover:bg-slate-200 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading ? "Analyzing..." : "Analyze Transaction"}
      </button>

      {error && (
        <p className="mt-4 text-sm text-red-400">
          {error}
        </p>
      )}
    </div>
  );
}