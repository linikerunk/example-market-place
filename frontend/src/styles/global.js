import styled, { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    font-size: 1.6rem;
    background-color: #F8F8F8;
    font-family: 'Poppins', sans-serif;
  }

  html {
    font-size: 62.5%;
  }

`;

export const Container = styled.div`
  max-width: 120rem;
  width: 100%;
  margin: 0 auto;
`;
