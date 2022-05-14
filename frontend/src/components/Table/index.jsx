import { Flex } from "../Vendas/styles";
import { Input } from "../Input";

import * as S from "./style";

export function Table() {
    return (
    <>
    <S.Container>
        <S.TitlePag> Produtos </S.TitlePag>
        <Flex>
            <Input
                widthInput={"30rem"}
                type={"text"}
                text={"Buscar pelo código de barras ou descição"}
            />
            <Input
                type={"number"}
                widthInput={"15rem"}
                min={0}
                text={"Quantidade de itens"}
            />
        </Flex>
    </S.Container>
    </>
    )
}