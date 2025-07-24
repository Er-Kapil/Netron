import React, { useState } from "react";
import { Power } from "lucide-react";
import Loader from "../components/Loader";
import { assets } from "../assets/ass.js";




const Home = () => {
  const [connect, setConnect] = useState(false);
  const [loading, setLoading] = useState(false);
  const handlePowerButton = async () => {
    setLoading(true);
    await new Promise((resolve) => setTimeout(resolve, 2000));
    setConnect(!connect);
    setLoading(false);
  };
  return (
    // Parent div
    <div className="h-screen relative">

      {/* Div containing the netron icon and the welcome message */}
      <div
        className={`flex flex-col justify-evenly h-screen ${
          loading ? "blur-sm" : ""
        }`}
      >
        <div className="flex flex-col items-center justify-center ">
          <h1 className="text-white text-md md:text-3xl ml-12">Welcome to</h1>
          <div className="flex gap-2">
            <img
              src={assets.iconn}
              alt=""
              className="rounded-full md:w-28 w-10 h-10 md:h-28"
            />
            <h1
              className="text-white text-4xl md:text-8xl font-serif antialiased italic font-thin font-stretch-extra-expanded"
            >
              NetrOn
            </h1>
          </div>
        </div>
        
        {/* Div containing the power button */}
        <div className="flex flex-col items-center justify-center ">
          {connect?  <p className="text-white">Connected</p> : <p className="text-white">Tap to connect</p>}


          <div
            className={`${
              connect ? "bg-gray-300 " : "bg-gray-500 hover:bg-gray-400"
            } w-25 md:w-40 flex items-center justify-center rounded-4xl cursor-pointer my-2`}
            onClick={handlePowerButton}
          >
            <Power
              color={connect ? "#292929" : "white"}
              strokeWidth={"3px"}
              className="my-1 size-5  md:size-12"
            />
          </div>
        </div>
      </div>
      {/* contains the loader that appears while loading only and the background goes blur */}
      {loading && (
        <div className="absolute top-1/2 left-[43%] ">
          <Loader />
        </div>
      )}
    </div>
  );
};

export default Home;
