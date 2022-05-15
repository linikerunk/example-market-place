import * as S from "./styles";

export function Button({ children, color, click }) {
  return (
    <>
      <S.Button colorButton={color} onClick={click}>{children}</S.Button>
    </>
  );
}
