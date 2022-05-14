import styled, { css } from "styled-components";

export const Button = styled.button`
  ${({ colorButton }) => css`
    background-color: ${colorButton};
    color: #fff;
    border: none;
    padding: 1rem 2rem;
    border-radius: 0.4rem;
    cursor: pointer;
    transition: all 0.2s ease;

    &:hover {
      transform: scale(1.1);
    }
  `}
`;