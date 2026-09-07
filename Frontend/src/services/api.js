const API_URL = import.meta.env.VITE_API_URL;

export async function searchVideos(query) {
  const response = await fetch(
    `${API_URL}/search/?q=${encodeURIComponent(query)}`
  );

  if (!response.ok) {
    throw new Error("Could not fetch videos");
  }

  const data = await response.json();

  return data;
}