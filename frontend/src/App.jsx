import { Home } from "./components/Home";
import { useEffect } from 'react';
import Aos from 'aos'
import "aos/dist/aos.css";

function App() {
  useEffect(() => {
    Aos.init({ duration: 1000 });
  }, [])
  return (
    <>
      <Home />
    </>
  )
}

export default App;
