import { useState } from 'react'
import './App.css'


export function App() {
  const [originalUrl, setOriginalUrl] = useState("");
  // const [isOneTime, setIsOneTime] = useState(false);
  const [shortUrl, setShortUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [showAlert, setShowAlert] = useState(false);
  const [error, setError] = useState("");
  const BASE_URL = "https://snaplink-production.up.railway.app/api/v1/urls/";

  const handleShorten = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await fetch(BASE_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ original_url: originalUrl })
      });
      const data = await response.json();
      if (response.ok) {
        setShortUrl(data.new_url);
      } else {
        setError(data.error || "Failed to shorten URL");
      }
      setOriginalUrl("");
    } catch (err) {
      setError("Network error. Please try again.");
    }
    setLoading(false);
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(shortUrl);
    setShowAlert(true);

    // Hide alert after 3 seconds
    setTimeout(() => {
      setShowAlert(false);
    }, 3000);
  };

  return (
    <>
      <nav className="bg-indigo-700 w-full p-4 shadow-md">
        <div className="container mx-auto flex justify-between items-center">
          <a href="#" className="text-white text-lg font-bold">Snap Link</a>
          <div className="flex items-center space-x-4">
            <a href="#" className="text-white"><i className="fas fa-user"></i></a>
            <a href="#" className="text-white"><i className="fas fa-sign-in-alt"></i></a>
          </div>
        </div>
      </nav>
      <div className="min-h-[90vh] flex flex-col items-center pt-8">
        <div className="w-full max-w-lg p-8">
          <h1 className="text-4xl font-bold text-center mb-10">Snap Link - URL Shortener</h1>
          <form id="urlForm" className="space-y-9">
            <div>
              <label htmlFor="originalUrl" className="block text-xl font-semibold text-gray-700 pb-2">Paste your long link here</label>
              <input type="url" id="originalUrl" name="originalUrl" className="mt-1 block w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                value={originalUrl}
                onChange={(e) => setOriginalUrl(e.target.value)}
                placeholder="https://example.com" required />
            </div>

            {/* <div className="flex items-center">
              <input id="oneTime" name="oneTime" type="checkbox" className="h-4 w-4 text-indigo-600 border-gray-300 rounded" />
              <label htmlFor="oneTime" className="ml-2 block text-lg text-gray-900">Enable one-time use</label>
            </div>
            <div>
              <label htmlFor="expiryDate" className="block text-lg font-medium text-gray-700">Expiry Date</label>
              <input type="date" id="expiryDate" name="expiryDate" className="mt-1 block w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" />
            </div> */}
            <div>
              <button type="submit" className="w-full bg-indigo-600 text-white py-3 px-4 rounded-md shadow-sm hover:bg-indigo-700 disabled:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500" disabled={loading || !originalUrl} onClick={handleShorten}>
                {loading ? "Shortening..." : "Shorten URL"} <i className="fas fa-arrow-right ml-2"></i>
              </button>
            </div>
          </form>



          {showAlert && (
            <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-md mt-4 mb-4 text-xs text-center">
              Short URL copied successfully!
            </div>
          )}

          {shortUrl && (
            <div id="result" className="mt-10">
              <p className="text-lg text-gray-700">Your shortened URL:</p>
              <div className="flex items-center mt-2">
                <input type="text" id="shortenedUrl" className="w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" value={shortUrl} readOnly />
                <button onClick={handleCopy} id="copyButton" className="ml-2 bg-indigo-600 text-white py-3 px-4 rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                  <i className="fas fa-copy"></i>
                </button>
              </div>
            </div>
          )}

          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-md mt-4 mb-4 text-xs text-center">
              {error}
            </div>
          )}
        </div>
      </div>
    </>
  );
}


export default App
