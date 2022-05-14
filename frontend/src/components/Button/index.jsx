import * as S from "./styles";

export function Button({ children, color }) {
  return (
    <>
      <S.Button colorButton={color}>{children}</S.Button>
    </>
  );
}
