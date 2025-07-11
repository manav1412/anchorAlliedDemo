import React from 'react'
import { Toaster } from 'react-hot-toast'
import {createBrowserRouter, Route, RouterProvider} from "react-router-dom"
import Onboarding from './pages/Onboarding'
import Home from './pages/Home'
import RagSearch from './pages/RagSearch'
import Invoices from './pages/Invoices'

const router = createBrowserRouter([
  {
    path:"/",
    element:<Onboarding/>
  },
  {
    path:'/home',
    element:<Home/>
  },
  {
    path:'/invoices',
    element:<Invoices/>
  },
  {
    path:'/rag-search',
    element:<RagSearch/>
  }
])

const App = () => {
  return (
    <div>
      <RouterProvider router={router}></RouterProvider>
      <Toaster/>
      </div>
  )
}

export default App
