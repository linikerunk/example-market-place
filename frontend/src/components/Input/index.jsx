import * as S from "./style";

export function Input({ text, type, min, widthInput }) {
  return (
    <S.Wrapper>
      <span>{text}</span>
      <S.Input widthInput={widthInput} type={type} min={min} />
    </S.Wrapper>
  );
}
