import styled, { css } from "styled-components";

export const Title = styled.h1``;

export const Wrapper = styled.div`
  display: flex;
  width: 40rem;
  justify-content: space-between;
  flex-direction: column;
  height: 60rem;
  padding-left: 6rem;
  border-left: 1px solid #ddd;
`;

export const Box = styled.div`
  display: flex;
  flex-direction: column;
  margin-bottom: 20rem;
`;

export const Items = styled.div`
  display: flex;
  flex-direction: column;
  margin-top: 2rem;
`;

export const Flex = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

export const Label = styled.label`
  font-weight: bold;
  font-size: 1.3rem;
  color: gray;
  margin-bottom: 0.5rem;
`;

export const PriceTotal = styled.h3`
  margin-bottom: 2rem;
  font-size: 1.6rem;
  color: gray;
`;

export const Price = styled.h3`
  margin-left: 5rem;
  margin-bottom: 2rem;
  font-size: 1.6rem;
  color: gray;
`;

export const Select = styled.select`
  padding: 0.7rem 2rem;
  border: none;
  outline: none;
  background-color: #fff;
  border: 2px solid #d3d3d3;
`;

export const Footer = styled.div`
  display: flex;
  flex-direction: column;
  margin-bottom: 2rem;
`;
