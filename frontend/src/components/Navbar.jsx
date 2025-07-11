import React from 'react';
import { NavLink } from 'react-router-dom';
import "../../styles.css";

const Navbar = () => {
  return (
    <nav className="bg-blue-500 px-8 py-4 shadow-md">
      <div className="container mx-auto flex justify-end items-center space-x-4 text-lg">
        <NavLink
          to="/"
          className={({ isActive }) =>
            `px-4 py-2 rounded-md transition font-medium ${
              isActive ? 'bg-blue-700 text-white' : 'text-white hover:bg-blue-600'
            }`
          }
        >
          Onboarding
        </NavLink>
        <NavLink
          to="/home"
          className={({ isActive }) =>
            `px-4 py-2 rounded-md transition font-medium ${
              isActive ? 'bg-blue-700 text-white' : 'text-white hover:bg-blue-600'
            }`
          }
        >
          Home
        </NavLink>
        <NavLink
          to="/invoices"
          className={({ isActive }) =>
            `px-4 py-2 rounded-md transition font-medium ${
              isActive ? 'bg-blue-700 text-white' : 'text-white hover:bg-blue-600'
            }`
          }
        >
          Invoices
        </NavLink>
        {/* <NavLink
          to="/rag-search"
          className={({ isActive }) =>
            `px-4 py-2 rounded-md transition font-medium ${
              isActive ? 'bg-blue-700 text-white' : 'text-white hover:bg-blue-600'
            }`
          }
        >
          RAG Search
        </NavLink> */}
      </div>
    </nav>
  );
};

export default Navbar;
