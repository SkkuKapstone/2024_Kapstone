import React, { useState, useEffect } from "react";

const LeftSide = () => {
  const [text, setText] = useState("");
  const fullText =
    "Meet your own AI Studymate!\nUpload your documents, and a more accurate and secure personalized chatbot is born";

  useEffect(() => {
    let i = 0;
    const typingInterval = setInterval(() => {
      if (i < fullText.length) {
        setText(fullText.slice(0, i + 1));
        i++;
      } else {
        clearInterval(typingInterval);
      }
    }, 50);

    return () => clearInterval(typingInterval);
  }, []);

  return (
    <div className="flex flex-col items-center justify-center w-full lg:w-3/5 min-h-screen bg-gray-900 overflow-y-auto p-6">
      <h1 className="text-4xl md:text-6xl font-bold mb-6 text-center relative">
        <span className="bg-clip-text text-transparent bg-gradient-to-r from-[#ff6c0f] to-[#8dc63f] animate-pulse">
          Perfect StudyMate
        </span>
      </h1>
      <div className="w-24 h-px bg-gradient-to-r from-[#ff6c0f] to-[#8dc63f] my-4"></div>
      <p className="text-lg md:text-xl mb-10 text-center h-24 md:h-20 text-white mx-4 md:mx-8 lg:mx-16 whitespace-pre-line">
        {text}
      </p>
      <p className="text-xm md:text-sm text-gray-300 text-opacity-75">
        Team Kapstone from SKKU
      </p>
    </div>
  );
};

export default LeftSide;
