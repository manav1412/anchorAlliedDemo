import { useState } from 'react';
import axios from 'axios';
import toast from 'react-hot-toast';
import '../App.css';
import Navbar from '../components/Navbar';

function Home() {
  const [fileData, setFileData] = useState(null);
  const [responseData, setResponseData] = useState(null);
  const [islocalClicked, setLocalCLicked] = useState(false);
  const [isCloudClicked, setCloudClicked] = useState(false);
  const [previewUrl, setPreviewUrl] = useState(null);

  const toastOptions = { duration: 2000, position:"top-center"};

  const handleLocal = () =>{
    if(islocalClicked){
      setLocalCLicked(false)
    }
    else{
      setLocalCLicked(true)
      setCloudClicked(false)
    }
  }

  const handleCloud = () =>{
    if(isCloudClicked){
      setCloudClicked(false)
    }else{
      setCloudClicked(true)
      setLocalCLicked(false)
    }
  }

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    setFileData(file);
    setPreviewUrl(URL.createObjectURL(file));
    toast.success('File selected', toastOptions);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!fileData) {
      toast.error('Please upload a file first', toastOptions);
      return;
    }

    const formData = new FormData();
    formData.append('file', fileData);
    setFileData(null);

    const toastId = toast.loading('Uploading and parsing...', {
      duration: Infinity,
      position: 'top-right',
    });

    try {
      if(islocalClicked){
        const response = await axios.post(`${import.meta.env.VITE_API_URL}/upload`, formData);
        toast.success('Invoice parsed successfully!', { ...toastOptions, id: toastId });
        setResponseData(response.data.response);
      }else{
        const response = await axios.post(`${import.meta.env.VITE_API_URL}/upload-cloud`, formData);
        toast.success("Invoice parsed successfully!", { ...toastOptions, id: toastId});
        setResponseData(response.data.response);
      }
    } catch (err) {
      toast.error('Failed to parse invoice', { ...toastOptions, id: toastId });
      console.error('Parse Error:', err);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-100 to-white text-gray-800">
      <Navbar />

      <div className="max-w-5xl mx-auto px-4 py-12">
        <h1 className="text-5xl font-extrabold mb-4 text-center text-blue-700">Invoice Parser</h1>
        <p className="text-center text-lg mb-8 text-gray-700">
          Upload invoices or bills in <strong>PDF, DOCX, PNG, JPG</strong> formats. <br />
          Our system extracts both handwritten and printed content and returns a structured JSON.
        </p>

        <div className="flex justify-center gap-4 mb-6">
          <button
            className={`px-6 py-2 rounded-full font-semibold transition duration-200 shadow-md ${islocalClicked ? 'bg-blue-600 text-white' : 'bg-white text-blue-700 border border-blue-500'
              }`}
            onClick={handleLocal}
          >
            Parse Locally
          </button>
          <button
            className={`px-6 py-2 rounded-full font-semibold transition duration-200 shadow-md ${isCloudClicked ? 'bg-blue-600 text-white' : 'bg-white text-blue-700 border border-blue-500'
              }`}
            onClick={handleCloud}
          >
            Parse via Cloud
          </button>
        </div>

        <div className="bg-white rounded-2xl p-8 shadow-xl border border-gray-200">
          <h2 className="text-2xl font-bold mb-4 text-center text-blue-800">Upload your file</h2>

          <ul className="list-disc list-inside mb-6 text-sm text-gray-600 pl-4">
            <li>Supported formats: <strong>.pdf, .docx, .jpg, .jpeg, .png</strong></li>
            <li>File is parsed using an <strong>LLM</strong> model</li>
            <li>Data is extracted and stored securely</li>
            <li>You’ll see the parsed invoice in a structured format below</li>
          </ul>

          <form onSubmit={handleSubmit} className="space-y-4">
            <input
              type="file"
              accept='.png,.jpg,.jpeg,.pdf,.docx,.doc'
              onChange={handleUpload}
              className="block w-full text-sm text-gray-600
            file:mr-4 file:py-2 file:px-4
            file:rounded-full file:border-0
            file:text-sm file:font-semibold
            file:bg-blue-100 file:text-blue-700
            hover:file:bg-blue-200 transition duration-200"
            />

            {previewUrl && (
              <div className="mt-4 text-center">
                <p className="text-sm text-gray-600 mb-2">📷 File Preview</p>
                <img
                  src={previewUrl}
                  alt="Uploaded Preview"
                  className="mx-auto max-h-200 w-170 rounded-lg shadow border"
                />
              </div>
            )}

            <button
              type="submit"
              className="w-full bg-blue-600 text-white font-semibold py-3 rounded-lg hover:bg-blue-700 transition duration-300 shadow-md"
            >
              Parse Invoice
            </button>
          </form>
        </div>

        {responseData && typeof responseData === 'object' && (
          <div className="mt-12 bg-white p-8 rounded-2xl shadow-lg border border-gray-200">
            <h3 className="text-2xl font-bold mb-6 border-b pb-2 text-blue-800">Parsed Invoice Data</h3>

            <div className="grid md:grid-cols-2 gap-6 text-sm">
              <div>
                <p className="font-semibold text-gray-700">📅 Date</p>
                <p>{responseData.date || 'N/A'}</p>
              </div>

              <div>
                <p className="font-semibold text-gray-700">📄 Bill ID</p>
                <p>{responseData.bill_id || 'N/A'}</p>
              </div>

              <div>
                <p className="font-semibold text-gray-700">🏢 Distributor Name</p>
                <p>{responseData.distributor_name || 'N/A'}</p>
              </div>

              <div>
                <p className="font-semibold text-gray-700">💰 Total Cost</p>
                <p>{responseData.total_cost ? `₹${responseData.total_cost}` : 'N/A'}</p>
              </div>
            </div>

            <div className="mt-8">
              <p className="font-semibold mb-3 text-gray-700">🧾 Product Details</p>
              <div className="overflow-x-auto">
                <table className="min-w-full text-sm border border-gray-300 rounded-md overflow-hidden">
                  <thead className="bg-blue-100 text-blue-900">
                    <tr>
                      <th className="px-4 py-2 border">Product</th>
                      <th className="px-4 py-2 border">Quantity</th>
                      <th className="px-4 py-2 border">Unit Price</th>
                      <th className="px-4 py-2 border">Total Price</th>
                    </tr>
                  </thead>
                  <tbody className="bg-white text-gray-800">
                    {responseData.each_product_prize?.map((item, idx) => (
                      <tr key={idx} className="border-t hover:bg-gray-50">
                        <td className="px-4 py-2 border">{item.product_name}</td>
                        <td className="px-4 py-2 border">{item.quantity}</td>
                        <td className="px-4 py-2 border">{item.unit_price}</td>
                        <td className="px-4 py-2 border">{item.total_price}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Home;
