import { useState, useEffect } from "react";

const Home = () => {
  const [imgLink, setImgLink] = useState("");
  const [dateValue, setDateValue] = useState("");
  let data = {};

  const handleSubmit = (e) => {
    e.preventDefault();
    data = {
      date: dateValue,
    };

    fetch("http://localhost:5000/getPredictionImage", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setImgLink(data.url);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <>
      <section class="forecast-banner w-full h-[200px] bg-cover bg-center bg-no-repeat">
        <div class="forecast-banner-overlay w-full h-full bg-gray-300 flex justify-center items-center">
          <div class="forecast-banner-content w-full max-w-7xl flex flex-col justify-center items-center">
            <h1 class="text-4xl font-bold text-black">Get forecast</h1>
            <form
              class="flex justify-center items-center mt-5"
              onSubmit={handleSubmit}
            >
              {/* Date input */}
              <input
                type="date"
                name="date"
                id="date"
                class="w-64 h-12 px-4 rounded-full bg-gray-200 focus:outline-none focus:bg-gray-500 transition"
                // the dates available are between 2023-11-20 and 2023-12-31
                min="2023-11-20"
                max="2023-12-31"
                value={dateValue}
                // on change, update the date value to the format YYYY-MM-DD
                onChange={(e) => setDateValue(e.target.value)}
              />
              <button
                type="submit"
                class="flex justify-center items-center w-12 h-12 ml-2 rounded-full bg-gray-200 hover:bg-gray-400 focus:outline-none focus:bg-gray-500 transition"
              >
                <svg
                  aria-hidden="true"
                  class="w-6 h-6 text-gray-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M21 21l-6.35-6.35M17 11a6 6 0 11-12 0 6 6 0 0112 0z"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                  ></path>
                </svg>
              </button>
              {/* Reset button */}
              <button
                type="reset"
                class="flex justify-center items-center w-12 h-12 ml-2 rounded-full bg-gray-200 hover:bg-gray-400 focus:outline-none focus:bg-gray-500 transition"
                onClick={() => {
                  setImgLink("");
                  setDateValue("");
                }}
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="21" height="21" viewBox="0 0 21 21">
                    <g fill="none" fill-rule="evenodd" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" transform="matrix(0 1 1 0 2.5 2.5)">
                        <path d="m3.98652376 1.07807068c-2.38377179 1.38514556-3.98652376 3.96636605-3.98652376 6.92192932 0 4.418278 3.581722 8 8 8s8-3.581722 8-8-3.581722-8-8-8" />
                        <path d="m4 1v4h-4" transform="matrix(1 0 0 -1 0 6)" />
                    </g>
                </svg>
              </button>
            </form>
          </div>
        </div>
      </section>
      {/* The image that will be displayed */}
      <div class="h-[500px] bg-cover bg-center bg-no-repeat">
        <img src={imgLink} alt="" />
      </div>
    </>
  );
};

export default Home;
