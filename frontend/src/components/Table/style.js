import styled, { css } from "styled-components";

export const Table = styled.table`
  margin-top: 2rem;

  height: 15rem;
  width: 100%;
`;

export const Columns = styled.tr``;

export const Title = styled.th`
  ${({ widthTitle }) => css`
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: left;
    color: #000;
    width: ${widthTitle};
  `}
`;

export const Items = styled.td`
  &:last-child {
    cursor: pointer;
  }

  svg {
    color: #e92929;
  }
`;

export const Container = styled.div`
  display: flex;
  flex-direction: column;
`;

export const TitlePag = styled.h2`
  margin-bottom: 4rem;
  font-weight: normal;
`;
