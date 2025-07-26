import React, { useState } from "react";
import { Waves } from "lucide-react";

const Vibration = () => {

    const [vibe, setVibe] = useState(20)
    
  return (
    <div className="bg-white w-1/4 ">
      <div className="text-white bg-blue-500">
        <p className="text-center text-2xl ">Normal</p>
      </div>
      <div>
        <h1 className="text-center font-bold text-xl">Vibration</h1>
        <div
          className={`flex justify-center items-center ${
            vibe > 70 ? "text-red-500" : ""
          } ${vibe < 30 ? "text-green-400" : ""} ${
            vibe > 30 && vibe < 70 ? "text-yellow-400" : ""
          }`}
        >
          <Waves className={`size-40 `} strokeWidth={1} />
        </div>
        <div
          className={`${vibe > 70 ? "text-red-500" : ""} ${
            vibe < 30 ? "text-green-400" : ""
          } ${
            vibe > 30 && vibe < 70 ? "text-yellow-400" : ""
          } text-center font-bold text-2xl`}
        >
          {vibe}&deg;C
        </div>
      </div>
    </div>
  );
};

export default Vibration;
