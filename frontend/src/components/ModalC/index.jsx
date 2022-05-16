import * as S from "./style";
import { AiOutlineClose } from "react-icons/ai";
import { Button } from "../Button";
import { API } from '../../services/api'

export function ModalC({ title, children, setIsOpen, api }) {
  async function getData() {
    const response = await API.post(api, {
      name: ''
    })
  }

  useEffect(() => {
    getData()
  }, [])

  return (
    <S.Wrapper>
      <S.Card>
        <S.ButtonClose onClick={() => setIsOpen((prev) => !prev)}>
          <AiOutlineClose />
        </S.ButtonClose>
        <S.Title>{title}</S.Title>
        <S.Content>{children}</S.Content>
        <S.ContainerButton>
          <Button type="submit" color={"#049237"}>
            Continuar
          </Button>
          <Button color={"#1137f1ed"} click={() => setIsOpen((prev) => !prev)}>
            Cancelar
          </Button>
        </S.ContainerButton>
      </S.Card>
      <S.Overlay />
    </S.Wrapper>
  );
}
