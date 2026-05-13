export default function HeroSection() {
  return (
    <section className="relative overflow-hidden border-b border-slate-800">
      {/* Background Gradient */}
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/10 via-cyan-500/5 to-transparent" />

      <div className="relative mx-auto max-w-7xl px-6 py-24 md:py-32">
        <div className="mx-auto max-w-4xl text-center">
          {/* Badge */}
          <div className="mb-6 inline-flex items-center rounded-full border border-slate-700 bg-slate-900/70 px-4 py-1.5 text-sm text-slate-300 backdrop-blur">
            Intelligent Financial Fraud Detection Platform
          </div>

          {/* Title */}
          <h1 className="mb-6 text-5xl font-bold tracking-tight md:text-7xl">
            FraudShield AI
          </h1>

          {/* Subtitle */}
          <p className="mx-auto mb-10 max-w-3xl text-lg leading-8 text-slate-300 md:text-xl">
            Detect fraudulent financial transactions using machine
            learning, anomaly detection, explainable AI, batch
            analytics, and downloadable investigation reports.
          </p>

          {/* Buttons */}
          <div className="flex flex-col items-center justify-center gap-4 sm:flex-row">
            <a
              href="#analyzer"
              className="rounded-2xl bg-white px-6 py-3 font-semibold text-slate-900 transition hover:bg-slate-200"
            >
              Analyze Transaction
            </a>

            <a
              href="http://localhost:8000/docs"
              target="_blank"
              rel="noreferrer"
              className="rounded-2xl border border-slate-700 px-6 py-3 font-semibold text-white transition hover:bg-slate-800"
            >
              API Documentation
            </a>
          </div>

          {/* Stats */}
          <div className="mt-16 grid grid-cols-2 gap-4 md:grid-cols-4">
            {[
              ["ROC-AUC", "0.98+"],
              ["PR-AUC", "0.87+"],
              ["Transactions", "284K+"],
              ["Fraud Cases", "492"],
            ].map(([label, value]) => (
              <div
                key={label}
                className="rounded-2xl border border-slate-800 bg-slate-900/70 p-4 backdrop-blur"
              >
                <div className="text-2xl font-bold">{value}</div>
                <div className="mt-1 text-sm text-slate-400">
                  {label}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}