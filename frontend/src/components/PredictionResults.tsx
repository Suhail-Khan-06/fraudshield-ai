interface RiskFactor {
  feature: string;
  impact: number;
}

interface PredictionResultsProps {
  result: {
    is_fraud: boolean;
    fraud_probability: number;
    anomaly_score: number;
    risk_score: number;
    severity: "Low" | "Medium" | "High" | "Critical";
    recommendations: string[];
    key_risk_factors: RiskFactor[];
  };
}

function getSeverityStyles(severity: string) {
  switch (severity) {
    case "Critical":
      return "bg-red-500/20 text-red-300 border-red-500/30";
    case "High":
      return "bg-orange-500/20 text-orange-300 border-orange-500/30";
    case "Medium":
      return "bg-yellow-500/20 text-yellow-300 border-yellow-500/30";
    default:
      return "bg-green-500/20 text-green-300 border-green-500/30";
  }
}

export default function PredictionResults({
  result,
}: PredictionResultsProps) {
  return (
    <div className="space-y-6">
      {/* Top Metrics */}
      <div className="grid gap-6 md:grid-cols-4">
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <div className="text-sm text-slate-400">Risk Score</div>
          <div className="mt-2 text-4xl font-bold">
            {result.risk_score}
          </div>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <div className="text-sm text-slate-400">Severity</div>
          <div
            className={`mt-3 inline-flex rounded-full border px-4 py-1 text-sm font-semibold ${getSeverityStyles(
              result.severity
            )}`}
          >
            {result.severity}
          </div>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <div className="text-sm text-slate-400">
            Fraud Probability
          </div>
          <div className="mt-2 text-2xl font-bold">
            {(result.fraud_probability * 100).toFixed(2)}%
          </div>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <div className="text-sm text-slate-400">
            Anomaly Score
          </div>
          <div className="mt-2 text-2xl font-bold">
            {result.anomaly_score.toFixed(3)}
          </div>
        </div>
      </div>

      {/* Recommendations */}
      <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
        <h3 className="mb-4 text-xl font-semibold">
          Recommended Actions
        </h3>

        <ul className="space-y-2 text-slate-300">
          {result.recommendations.map((recommendation, index) => (
            <li key={index}>• {recommendation}</li>
          ))}
        </ul>
      </div>

      {/* Key Risk Factors */}
      <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
        <h3 className="mb-4 text-xl font-semibold">
          Key Risk Factors
        </h3>

        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {result.key_risk_factors.map((factor) => (
            <div
              key={factor.feature}
              className="rounded-2xl bg-slate-950 p-4"
            >
              <div className="text-sm text-slate-400">
                {factor.feature}
              </div>
              <div className="mt-1 text-xl font-bold">
                {factor.impact.toFixed(4)}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}