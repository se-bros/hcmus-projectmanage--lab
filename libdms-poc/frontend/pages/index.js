import { useState, useRef } from "react";
import axios from "axios";
import Head from "next/head";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export default function Home() {
  const [file, setFile] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [status, setStatus] = useState("idle"); // idle | uploading | done | error
  const [result, setResult] = useState(null);
  const [documents, setDocuments] = useState([]);
  const [activeTab, setActiveTab] = useState("upload"); // upload | history
  const fileInputRef = useRef();

  // --- Drag & Drop handlers ---
  const handleDragOver = (e) => { e.preventDefault(); setIsDragging(true); };
  const handleDragLeave = () => setIsDragging(false);
  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    const dropped = e.dataTransfer.files[0];
    if (dropped) setFile(dropped);
  };

  // --- Upload handler ---
  const handleUpload = async () => {
    if (!file) return;
    setStatus("uploading");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const { data } = await axios.post(`${API_URL}/documents/upload`, formData);
      const detail = await axios.get(`${API_URL}/documents/${data.id}`);
      setResult(detail.data);
      setStatus("done");
    } catch (err) {
      setStatus("error");
      setResult({ text: err.response?.data?.detail || "Lỗi kết nối tới server." });
    }
  };

  // --- Load history ---
  const loadHistory = async () => {
    setActiveTab("history");
    const { data } = await axios.get(`${API_URL}/documents`);
    setDocuments(data);
  };

  return (
    <>
      <Head>
        <title>LibDMS POC — Số hóa tài liệu</title>
        <meta name="description" content="POC hệ thống số hóa thư viện LibDMS" />
      </Head>

      <div style={styles.page}>
        {/* Header */}
        <header style={styles.header}>
          <div style={styles.logo}>📚 LibDMS</div>
          <span style={styles.badge}>POC — Skeleton v0.1</span>
        </header>

        {/* Tabs */}
        <div style={styles.tabs}>
          <button
            style={activeTab === "upload" ? styles.tabActive : styles.tab}
            onClick={() => setActiveTab("upload")}
          >
            📤 Tải lên & OCR
          </button>
          <button
            style={activeTab === "history" ? styles.tabActive : styles.tab}
            onClick={loadHistory}
          >
            📋 Lịch sử
          </button>
        </div>

        <main style={styles.main}>
          {activeTab === "upload" && (
            <div style={styles.card}>
              <h2 style={styles.cardTitle}>Số hóa tài liệu mới</h2>
              <p style={styles.cardSub}>Tải lên file ảnh (PNG, JPEG) hoặc PDF để trích xuất văn bản tiếng Việt</p>

              {/* Drop zone */}
              <div
                style={{ ...styles.dropzone, ...(isDragging ? styles.dropzoneDragging : {}) }}
                onDragOver={handleDragOver}
                onDragLeave={handleDragLeave}
                onDrop={handleDrop}
                onClick={() => fileInputRef.current.click()}
              >
                <input
                  type="file"
                  accept=".png,.jpg,.jpeg,.pdf"
                  ref={fileInputRef}
                  style={{ display: "none" }}
                  onChange={(e) => setFile(e.target.files[0])}
                />
                {file ? (
                  <div>
                    <div style={styles.fileIcon}>📄</div>
                    <div style={styles.fileName}>{file.name}</div>
                    <div style={styles.fileSize}>{(file.size / 1024 / 1024).toFixed(2)} MB</div>
                  </div>
                ) : (
                  <div>
                    <div style={styles.uploadIcon}>☁️</div>
                    <div style={styles.dropText}>Kéo thả file vào đây hoặc click để chọn</div>
                    <div style={styles.dropHint}>PNG, JPEG, PDF — Tối đa 50MB</div>
                  </div>
                )}
              </div>

              {/* Upload button */}
              <button
                style={{ ...styles.btn, ...((!file || status === "uploading") ? styles.btnDisabled : {}) }}
                onClick={handleUpload}
                disabled={!file || status === "uploading"}
              >
                {status === "uploading" ? "⏳ Đang xử lý OCR..." : "🚀 Bắt đầu số hóa"}
              </button>

              {/* Result */}
              {status === "done" && result && (
                <div style={styles.result}>
                  <div style={styles.resultHeader}>
                    ✅ OCR hoàn tất — <strong>{result.filename}</strong>
                  </div>
                  <div style={styles.resultLabel}>Văn bản trích xuất được:</div>
                  <pre style={styles.resultText}>{result.text || "(Không nhận diện được văn bản)"}</pre>
                </div>
              )}

              {status === "error" && result && (
                <div style={{ ...styles.result, borderColor: "#ff4d4f", background: "#fff2f0" }}>
                  <div style={{ color: "#ff4d4f" }}>❌ Lỗi: {result.text}</div>
                </div>
              )}
            </div>
          )}

          {activeTab === "history" && (
            <div style={styles.card}>
              <h2 style={styles.cardTitle}>Lịch sử tài liệu đã số hóa</h2>
              {documents.length === 0 ? (
                <div style={styles.empty}>Chưa có tài liệu nào được tải lên trong phiên này.</div>
              ) : (
                <table style={styles.table}>
                  <thead>
                    <tr>
                      <th style={styles.th}>Tên file</th>
                      <th style={styles.th}>Trạng thái</th>
                      <th style={styles.th}>Xem trước văn bản</th>
                    </tr>
                  </thead>
                  <tbody>
                    {documents.map((doc) => (
                      <tr key={doc.id} style={styles.tr}>
                        <td style={styles.td}>{doc.filename}</td>
                        <td style={styles.td}>
                          <span style={styles.statusBadge}>✅ {doc.status}</span>
                        </td>
                        <td style={styles.td}>
                          <span style={styles.preview}>
                            {doc.text?.slice(0, 80) || "(trống)"}...
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          )}
        </main>

        <footer style={styles.footer}>
          LibDMS POC v0.1 · FastAPI + Next.js + Tesseract OCR
          · <a href={`${API_URL}/docs`} target="_blank" rel="noreferrer" style={styles.link}>Swagger API Docs</a>
        </footer>
      </div>
    </>
  );
}

// --- Inline styles ---
const styles = {
  page: { minHeight: "100vh", background: "#f0f4f8", fontFamily: "'Segoe UI', sans-serif", color: "#1a1a2e" },
  header: { background: "linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)", color: "white", padding: "16px 32px", display: "flex", alignItems: "center", gap: "16px", boxShadow: "0 2px 12px rgba(0,0,0,0.3)" },
  logo: { fontSize: "22px", fontWeight: "700", letterSpacing: "1px" },
  badge: { background: "rgba(255,255,255,0.15)", borderRadius: "20px", padding: "4px 12px", fontSize: "12px" },
  tabs: { background: "white", borderBottom: "2px solid #e8ecf0", display: "flex", padding: "0 32px", gap: "4px" },
  tab: { padding: "14px 20px", border: "none", background: "transparent", cursor: "pointer", fontSize: "14px", color: "#666", borderBottom: "2px solid transparent", marginBottom: "-2px" },
  tabActive: { padding: "14px 20px", border: "none", background: "transparent", cursor: "pointer", fontSize: "14px", color: "#0066cc", borderBottom: "2px solid #0066cc", marginBottom: "-2px", fontWeight: "600" },
  main: { padding: "32px", maxWidth: "900px", margin: "0 auto" },
  card: { background: "white", borderRadius: "12px", padding: "32px", boxShadow: "0 4px 20px rgba(0,0,0,0.08)" },
  cardTitle: { fontSize: "20px", fontWeight: "700", marginBottom: "6px", color: "#1a1a2e" },
  cardSub: { color: "#666", fontSize: "14px", marginBottom: "24px" },
  dropzone: { border: "2px dashed #c0ccda", borderRadius: "12px", padding: "48px 24px", textAlign: "center", cursor: "pointer", transition: "all 0.2s", background: "#fafbfc", marginBottom: "20px" },
  dropzoneDragging: { borderColor: "#0066cc", background: "#e6f0ff" },
  uploadIcon: { fontSize: "48px", marginBottom: "12px" },
  dropText: { fontSize: "16px", fontWeight: "600", color: "#333", marginBottom: "6px" },
  dropHint: { fontSize: "13px", color: "#888" },
  fileIcon: { fontSize: "48px", marginBottom: "8px" },
  fileName: { fontSize: "16px", fontWeight: "600", color: "#0066cc", marginBottom: "4px" },
  fileSize: { fontSize: "13px", color: "#888" },
  btn: { width: "100%", padding: "14px", background: "linear-gradient(135deg, #0066cc, #004999)", color: "white", border: "none", borderRadius: "8px", fontSize: "16px", fontWeight: "600", cursor: "pointer", transition: "opacity 0.2s" },
  btnDisabled: { opacity: 0.5, cursor: "not-allowed" },
  result: { marginTop: "24px", border: "1px solid #52c41a", borderRadius: "8px", background: "#f6ffed", padding: "16px" },
  resultHeader: { color: "#389e0d", marginBottom: "12px", fontSize: "14px" },
  resultLabel: { fontSize: "13px", color: "#666", marginBottom: "8px", fontWeight: "600" },
  resultText: { background: "#1a1a2e", color: "#a8ff78", padding: "16px", borderRadius: "8px", fontSize: "13px", lineHeight: "1.8", whiteSpace: "pre-wrap", wordBreak: "break-word", maxHeight: "400px", overflowY: "auto" },
  empty: { textAlign: "center", color: "#888", padding: "40px", fontSize: "15px" },
  table: { width: "100%", borderCollapse: "collapse" },
  th: { background: "#f5f7fa", padding: "12px 16px", textAlign: "left", fontSize: "13px", fontWeight: "600", color: "#555", borderBottom: "2px solid #e8ecf0" },
  tr: { borderBottom: "1px solid #f0f2f5" },
  td: { padding: "12px 16px", fontSize: "14px", verticalAlign: "top" },
  statusBadge: { background: "#f6ffed", color: "#52c41a", border: "1px solid #b7eb8f", borderRadius: "12px", padding: "2px 10px", fontSize: "12px" },
  preview: { color: "#666", fontStyle: "italic" },
  footer: { textAlign: "center", padding: "24px", color: "#999", fontSize: "13px", borderTop: "1px solid #e8ecf0", background: "white", marginTop: "32px" },
  link: { color: "#0066cc" },
};
