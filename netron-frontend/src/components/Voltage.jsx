import React, { useState } from "react";
import { Battery } from "lucide-react";


const Voltage = () => {
    const [volt, setVolt] = useState(20)
  return (
    <div className="bg-white w-1/4 ">
      <div className="text-white bg-blue-500">
        <p className="text-center text-2xl ">Normal</p>
      </div>
      <div>
        <h1 className="text-center font-bold text-xl">Voltage</h1>
        <div
          className={`flex justify-center items-center ${
            volt > 70 ? "text-red-500" : ""
          } ${volt < 30 ? "text-green-400" : ""} ${
            volt > 30 && volt < 70 ? "text-yellow-400" : ""
          }`}
        >
          <Battery className={`size-40 `} strokeWidth={1} />
        </div>
        <div
          className={`${volt > 70 ? "text-red-500" : ""} ${
            volt < 30 ? "text-green-400" : ""
          } ${
            volt > 30 && volt < 70 ? "text-yellow-400" : ""
          } text-center font-bold text-2xl`}
        >
          {volt}&deg;C
        </div>
      </div>
    </div>
  );
};

export default Voltage;
