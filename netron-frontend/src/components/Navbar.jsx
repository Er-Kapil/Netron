import React, { useState } from "react";
import { assets } from "../assets/ass.js";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const [connected, setConnected] = useState(false);
  const navigate = useNavigate();

  const  handleConnect = () => {
    if(connected){
        setConnected(false);
        navigate("/");
    }else{
        setConnected(true);
        navigate("/dashboard");
    }
  }
  return (
    <div className="flex gap-2 justify-around items-center bg-blue-500">
      <div className="flex justify-center items-center gap-5">
        <img
          src={assets.iconn}
          alt=""
          className="rounded-full md:w-13 w-10 h-10 md:h-13"
        />
        <h1 className="text-white text-3xl">NetrOn</h1>
      </div>
      <div>
        {connected ? (
          <div onClick={handleConnect} className="flex justify-center items-center gap-2">
            <div className="h-2 w-2 bg-green-500 rounded-full"></div>
            <p className="text-white md:text-md text-sm">Connected</p>
          </div>
        ) : (
          <div onClick={handleConnect} className="flex justify-center items-center gap-2">
            <div className="h-2 w-2 bg-red-500 rounded-full"></div>
            <p className="text-white md:text-md text-sm">Disconnected</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Navbar;
