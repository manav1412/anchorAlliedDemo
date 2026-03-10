import React, { useEffect, useState } from 'react';
import Navbar from '../components/Navbar';
import axios from 'axios';
import { ChevronDown, ChevronUp } from 'lucide-react';
import toast from 'react-hot-toast';

const Invoices = () => {
  const [allInvoices, setAllInvoices] = useState([]);
  const [expandedInvoice, setExpandedInvoice] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    const fetchInvoices = async () => {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/invoices`);
        setAllInvoices(response.data.invoices);
      } catch (err) {
        console.error("Error fetching invoices:", err);
      }
    };

    fetchInvoices();
  }, []);

  const handleSearch = (e) => {
    setSearchTerm(e.target.value.toLowerCase());
  };

  const handleDelete = async(invoiceId) =>{
    const confirmDelete = window.confirm("Are you sure you want to delete this invoice?")
    if(!confirmDelete){
      return;
    }

    try{
      const response = await axios.delete(`${import.meta.env.VITE_API_URL}/invoice/${invoiceId}`);
      if(response.data?.message){
        setAllInvoices((prev) => prev.filter((invoice) => invoice._id !== invoiceId));
        toast.success(response.data.message)
      }else{
        toast.error(response.data.error)
      }
    }catch(err){
      toast.error("Something went wrong")
    }
  } 

  const filteredInvoices = allInvoices.filter((invoice) =>
    invoice.bill_id?.toLowerCase().includes(searchTerm) ||
    invoice.distributor_name?.toLowerCase().includes(searchTerm)
  );

  const toggleExpand = (id) => {
    setExpandedInvoice(expandedInvoice === id ? null : id);
  };

  return (
    // <div className="min-h-screen bg-gray-100 text-gray-800">
    //   <Navbar />

    //   <div className="max-w-6xl mx-auto px-4 py-8">
    //     <h1 className="text-2xl font-bold mb-4 text-center">Invoices</h1>

    //     <input
    //       type="text"
    //       value={searchTerm}
    //       onChange={handleSearch}
    //       placeholder="Search by Bill ID or Distributor Name"
    //       className="mb-6 w-full p-3 rounded-lg border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
    //     />

    //     <div className="overflow-x-auto rounded-xl shadow">
    //       <table className="min-w-full bg-white">
    //         <thead className="bg-blue-600 text-white">
    //           <tr>
    //             <th className="py-3 px-4 text-left">Bill ID</th>
    //             <th className="py-3 px-4 text-left">Distributor</th>
    //             <th className="py-3 px-4 text-left">Date</th>
    //             <th className="py-3 px-4 text-left">Total Cost</th>
    //             <th className="py-3 px-4 text-left">Products</th>
    //             <th className="py-3 px-4 text-center">Details</th>
    //           </tr>
    //         </thead>
    //         <tbody>
    //           {filteredInvoices.length > 0 ? (
    //             filteredInvoices.map((invoice) => (
    //               <React.Fragment key={invoice._id}>
    //                 <tr className="border-t hover:bg-gray-50">
    //                   <td className="py-3 px-4">{invoice.bill_id}</td>
    //                   <td className="py-3 px-4">{invoice.distributor_name}</td>
    //                   <td className="py-3 px-4">{invoice.date ? new Date(invoice.date).toLocaleDateString() : 'N/A'}</td>
    //                   <td className="py-3 px-4">
    //                     {invoice.total_cost ? `₹${invoice.total_cost}` : 'N/A'}
    //                   </td>
    //                   <td className="py-3 px-4">{invoice.products?.length || 0}</td>
    //                   <td className="py-3 px-4 text-center">
    //                     <button
    //                       onClick={() => toggleExpand(invoice._id)}
    //                       className="text-blue-600 hover:text-blue-800 transition"
    //                     >
    //                       {expandedInvoice === invoice._id ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
    //                     </button>
    //                   </td>
    //                 </tr>

    //                 {/* Expanded Row */}
    //                 {expandedInvoice === invoice._id && (
    //                   <tr className="bg-gray-50">
    //                     <td colSpan="5" className="p-4">
    //                       <div className="overflow-x-auto">
    //                         <h3 className="font-semibold mb-2">Product Details</h3>
    //                         <table className="w-full text-sm border border-gray-200 rounded-md">
    //                           <thead className="bg-gray-100">
    //                             <tr>
    //                               <th className="border px-3 py-2 text-left">Product</th>
    //                               <th className="border px-3 py-2 text-left">Quantity</th>
    //                               <th className="border px-3 py-2 text-left">Unit Price</th>
    //                               <th className="border px-3 py-2 text-left">Total Price</th>
    //                             </tr>
    //                           </thead>
    //                           <tbody>
    //                             {invoice.each_product_prize?.map((item, idx) => (
    //                               <tr key={idx} className="border-t">
    //                                 <td className="border px-3 py-2">{item.product_name}</td>
    //                                 <td className="border px-3 py-2">{item.quantity}</td>
    //                                 <td className="border px-3 py-2">₹{item.unit_price}</td>
    //                                 <td className="border px-3 py-2">₹{item.total_price}</td>
    //                               </tr>
    //                             ))}
    //                           </tbody>
    //                         </table>
    //                       </div>
    //                     </td>
    //                   </tr>
    //                 )}
    //               </React.Fragment>
    //             ))
    //           ) : (
    //             <tr>
    //               <td colSpan="5" className="text-center py-6 text-gray-500">
    //                 No invoices found.
    //               </td>
    //             </tr>
    //           )}
    //         </tbody>
    //       </table>
    //     </div>
    //   </div>
    // </div>
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-white text-gray-800">
      <Navbar />

      <div className="max-w-7xl mx-auto px-4 py-10">
        <h1 className="text-4xl font-extrabold mb-6 text-center text-blue-700">Invoice Records</h1>

        <input
          type="text"
          value={searchTerm}
          onChange={handleSearch}
          placeholder="🔍 Search by Bill ID or Distributor Name"
          className="mb-8 w-full p-4 rounded-xl border border-gray-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400 text-sm"
        />

        <div className="overflow-x-auto rounded-xl shadow-lg border border-gray-200">
          <table className="min-w-full bg-white text-sm text-left">
            <thead className="bg-blue-600 text-white text-sm uppercase">
              <tr>
                <th className="py-3 px-5">Bill ID</th>
                <th className="py-3 px-5">Distributor</th>
                <th className="py-3 px-5">Date</th>
                <th className="py-3 px-5">Total Cost</th>
                <th className="py-3 px-5">Products</th>
                <th className="py-3 px-5 text-center">Details</th>
              </tr>
            </thead>
            <tbody>
              {filteredInvoices.length > 0 ? (
                filteredInvoices.map((invoice) => (
                  <React.Fragment key={invoice._id}>
                    <tr className="border-t hover:bg-gray-50 transition">
                      <td className="py-3 px-5">{invoice.bill_id}</td>
                      <td className="py-3 px-5">{invoice.distributor_name}</td>
                      <td className="py-3 px-5">{invoice.date ? invoice.date : 'N/A'}</td>
                      <td className="py-3 px-5">
                        {invoice.total_cost ? `₹${invoice.total_cost}` : 'N/A'}
                      </td>
                      <td className="py-3 px-5">{invoice.products?.length || 0}</td>
                      <td className="py-3 px-5 text-center flex items-center justify-center gap-2">
                        <button
                          onClick={() => toggleExpand(invoice._id)}
                          className="text-blue-600 hover:text-blue-800 transition duration-200"
                          title="Toggle Details"
                        >
                          {expandedInvoice === invoice._id ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
                        </button>
                        <button
                          onClick={() => handleDelete(invoice._id)}
                          className="text-red-500 hover:text-red-700 transition duration-200"
                          title="Delete Invoice"
                        >
                          🗑
                        </button>
                      </td>

                      {/* 
                       */}
                    </tr>

                    {/* Expanded Row */}
                    {expandedInvoice === invoice._id && (
                      <tr className="bg-gray-50 transition-all">
                        <td colSpan="6" className="px-6 py-4">
                          <div className="bg-white border rounded-lg p-4 shadow-inner">
                            <h3 className="text-base font-semibold text-gray-700 mb-2">🧾 Product Details</h3>
                            <div className="overflow-x-auto">
                              <table className="w-full border border-gray-200 text-sm">
                                <thead className="bg-gray-100 text-gray-700">
                                  <tr>
                                    <th className="border px-4 py-2 text-left">Product</th>
                                    <th className="border px-4 py-2 text-left">Quantity</th>
                                    <th className="border px-4 py-2 text-left">Unit Price</th>
                                    <th className="border px-4 py-2 text-left">Total Price</th>
                                  </tr>
                                </thead>
                                <tbody>
                                  {invoice.each_product_prize?.map((item, idx) => (
                                    <tr key={idx} className="hover:bg-gray-50 border-t">
                                      <td className="border px-4 py-2">{item.product_name}</td>
                                      <td className="border px-4 py-2">{item.quantity}</td>
                                      <td className="border px-4 py-2">₹{item.unit_price}</td>
                                      <td className="border px-4 py-2">₹{item.total_price}</td>
                                    </tr>
                                  ))}
                                </tbody>
                              </table>
                            </div>
                          </div>
                        </td>
                      </tr>
                    )}
                  </React.Fragment>
                ))
              ) : (
                <tr>
                  <td colSpan="6" className="text-center py-10 text-gray-500">
                    No invoices found.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Invoices;
