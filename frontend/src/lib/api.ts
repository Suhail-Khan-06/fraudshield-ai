import axios from "axios";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export const api = axios.create({
  baseURL: `${API_BASE_URL}/api/v1`,
  headers: {
    "Content-Type": "application/json",
  },
});

// -----------------------------------------------------
// Types
// -----------------------------------------------------

export interface RiskFactor {
  feature: string;
  impact: number;
}

export interface PredictionResponse {
  is_fraud: boolean;
  fraud_probability: number;
  anomaly_score: number;
  risk_score: number;
  severity: "Low" | "Medium" | "High" | "Critical";
  recommendations: string[];
  key_risk_factors: RiskFactor[];
}

export interface BatchResponse {
  total_transactions: number;
  fraud_predictions: number;
  average_risk_score: number;
  severity_distribution: Record<string, number>;
  results: PredictionResponse[];
}

// -----------------------------------------------------
// API Methods
// -----------------------------------------------------

export async function predictTransaction(
  transaction: Record<string, number>
): Promise<PredictionResponse> {
  const response = await api.post<PredictionResponse>(
    "/predict",
    transaction
  );
  return response.data;
}

export async function uploadCsv(
  file: File
): Promise<BatchResponse> {
  const formData = new FormData();
  formData.append("file", file);

  const response = await api.post<BatchResponse>(
    "/predict/csv",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
}

export async function downloadPdf(
  transaction: Record<string, number>
): Promise<Blob> {
  const response = await api.post(
    "/report/pdf",
    transaction,
    {
      responseType: "blob",
    }
  );

  return response.data;
}