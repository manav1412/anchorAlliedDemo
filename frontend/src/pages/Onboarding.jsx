import React from 'react';
import Navbar from '../components/Navbar';

const Onboarding = () => {
  return (
    <div className="bg-blue-500 min-h-screen text-white">
      <Navbar />
      <div className="max-w-6xl mx-auto px-6 py-12">
        <h1 className="text-4xl font-bold mb-6">Welcome to InvoiceAI</h1>
        <p className="text-lg mb-10 leading-relaxed">
          Our platform helps you extract structured data from invoices and bills—whether printed or handwritten—
          using powerful local LLMs. View, search, and interact with your data in real-time.
        </p>

        <div className="grid md:grid-cols-2 gap-6">
          {/* Feature Card */}
          <div className="bg-white text-blue-500 rounded-2xl shadow-lg p-8">
            <h2 className="text-xl font-semibold mb-2">📤 Multi-format Upload</h2>
            <p>Upload PDF, DOCX, or image-based invoices and bills for automated parsing.</p>
          </div>

          {/* Feature Card */}
          <div className="bg-white text-blue-500 rounded-2xl shadow-lg p-6">
            <h2 className="text-xl font-semibold mb-2">🧠 OCR + LLM Extraction</h2>
            <p>Extracts handwritten and printed text using OCR, then structures it via a locally running model</p>
          </div>

          {/* Feature Card */}
          <div className="bg-white text-blue-500 rounded-2xl shadow-lg p-8">
            <h2 className="text-xl font-semibold mb-2">🗂️ MongoDB Storage</h2>
            <p>Data is stored in a strict JSON format and saved in MongoDB for easy access and performance.</p>
          </div>

          {/* Feature Card */}
          <div className="bg-white text-blue-500 rounded-2xl shadow-lg p-6">
            <h2 className="text-xl font-semibold mb-2">📊 Dashboard & Search</h2>
            <p>Search invoices by Bill ID or Distributor Name on a sleek, responsive dashboard.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Onboarding;
