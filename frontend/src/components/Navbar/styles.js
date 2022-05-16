import styled from "styled-components";

export const Header = styled.header`
  display: flex;
  align-items: center;
  background-color: #f0f0f0;
  width: 100%;
  height: 6rem;
  box-shadow: rgb(3 3 3 / 10%) 0px 3px 3px;
  margin-bottom: 2rem;
`;

export const Wrapper = styled.div`
  display: flex;
  justify-content: space-between;
  width: 100%;
  align-items: center;

  h1 {
    display: flex;
    align-self: center;
    color: #007a4f;
  }
`;
