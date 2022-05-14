import styled, { css } from "styled-components";

export const Title = styled.h1``;

export const Wrapper = styled.div`
  display: flex;
  width: 40rem;
  justify-content: space-between;
  flex-direction: column;
  height: calc(100vh - 7rem);
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