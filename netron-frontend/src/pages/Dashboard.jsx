import React from 'react'
import Navbar from '../components/Navbar.jsx'
import Temperature from '../components/Temperature.jsx'
import Voltage from '../components/Voltage.jsx'
import Vibration from '../components/Vibration.jsx'

const Dashboard = () => {
  return (
    <div>
      <Navbar />

      <div className='my-10'>
        <h1 className='text-white text-3xl text-center my-10'>Live Data</h1>
        <div className='flex justify-around'>
          <Temperature />
          <Vibration />
          <Voltage />
        </div>
      </div>
    </div>
  )
}

export default Dashboard
