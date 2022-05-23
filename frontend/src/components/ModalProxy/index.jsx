import * as S from "./style";
import { AiOutlineClose } from "react-icons/ai";
import { Button } from "../Button";
import { API } from '../../services/api'

export function ModalC({ title, children, setIsOpen, api, valueInput }) {
  async function sendPost() {
    const response = await API.post(api, {
      name: valueInput
    })
  }


  return (
    <S.Wrapper>
      <S.Card>
        <S.ButtonClose onClick={() => setIsOpen((prev) => !prev)}>
          <AiOutlineClose />
        </S.ButtonClose>
        <S.Title>{title}</S.Title>
        <S.Content>{children}</S.Content>
        <S.ContainerButton>
          <button onClick={sendPost} color={"#049237"}>
            Continuar
          </button>
          <Button color={"#1137f1ed"} click={() => setIsOpen((prev) => !prev)}>
            Cancelar
          </Button>
        </S.ContainerButton>
      </S.Card>
      <S.Overlay />
    </S.Wrapper>
  );
}
