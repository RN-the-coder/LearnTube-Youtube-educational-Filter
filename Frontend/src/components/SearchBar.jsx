import { useState } from "react";
import { useNavigate } from "react-router-dom";

function SearchBar({ initialValue = "" }) {
  const [query, setQuery] = useState(initialValue);
  const navigate = useNavigate();

  const handleSubmit = (event) => {
    event.preventDefault();

    const cleanQuery = query.trim();

    if (!cleanQuery) return;

    navigate(`/search?q=${encodeURIComponent(cleanQuery)}`);
  };

  return (
    <form className="search-form" onSubmit={handleSubmit}>
      <input
        className="search-input"
        type="text"
        placeholder="What do you want to learn?"
        value={query}
        onChange={(event) => setQuery(event.target.value)}
        autoComplete="off"
      />

      <button className="search-button" type="submit">
        Search
      </button>
    </form>
  );
}

export default SearchBar;