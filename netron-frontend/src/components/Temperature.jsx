import React, { useState } from "react";
import { Thermometer } from "lucide-react";

const Temperature = () => {
  const [temp, setTemp] = useState(50);
  return (
    <div className="bg-white w-1/4 ">
      <div className="text-white bg-blue-500">
        <p className="text-center text-2xl ">cool</p>
      </div>
      <div>
        <h1 className="text-center font-bold text-xl">Temperature</h1>
        <div className={`flex justify-center items-center ${temp > 70 ?"text-red-500":""} ${temp<30?"text-green-400":""} ${temp>30 && temp<70?"text-yellow-400":""}`}>
          <Thermometer className={`size-40 `} strokeWidth={1} />
        </div>
        <div
          className={`${temp > 70 ? "text-red-500" : ""} ${
            temp < 30 ? "text-green-400" : ""
          } ${
            temp > 30 && temp < 70 ? "text-yellow-400" : ""
          } text-center font-bold text-2xl`}
        >
          {temp}&deg;C
        </div>
      </div>
    </div>
  );
};

export default Temperature;
