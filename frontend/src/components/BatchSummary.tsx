import { BatchResponse } from "@/lib/api";

interface BatchSummaryProps {
  result: BatchResponse;
}

export default function BatchSummary({
  result,
}: BatchSummaryProps) {
  return (
    <div className="space-y-6">
      {/* Summary Cards */}
      <div className="grid gap-6 md:grid-cols-4">
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <div className="text-sm text-slate-400">
            Total Transactions
          </div>
          <div className="mt-2 text-3xl font-bold">
            {result.total_transactions.toLocaleString()}
          </div>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <div className="text-sm text-slate-400">
            Fraud Predictions
          </div>
          <div className="mt-2 text-3xl font-bold text-red-400">
            {result.fraud_predictions}
          </div>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <div className="text-sm text-slate-400">
            Average Risk Score
          </div>
          <div className="mt-2 text-3xl font-bold">
            {result.average_risk_score}
          </div>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <div className="text-sm text-slate-400">
            Critical Alerts
          </div>
          <div className="mt-2 text-3xl font-bold text-red-400">
            {result.severity_distribution.Critical || 0}
          </div>
        </div>
      </div>

      {/* Severity Distribution */}
      <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
        <h3 className="mb-4 text-xl font-semibold">
          Severity Distribution
        </h3>

        <div className="grid gap-4 md:grid-cols-4">
          {Object.entries(
            result.severity_distribution
          ).map(([severity, count]) => (
            <div
              key={severity}
              className="rounded-2xl bg-slate-950 p-4"
            >
              <div className="text-sm text-slate-400">
                {severity}
              </div>
              <div className="mt-1 text-2xl font-bold">
                {count}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}