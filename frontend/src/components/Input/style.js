import styled, { css } from "styled-components";

export const Input = styled.input`
  ${({ widthInput }) => css`
    border: 2px solid #d3d3d3;
    padding: 1rem;
    outline: none;
    width: ${widthInput};
    margin-right: 2rem;
  `}
`;

export const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  position: relative;

  span {
    font-weight: bold;
    font-size: 1.3rem;
    position: absolute;
    bottom: 40px;
    color: gray;
  }
`;
