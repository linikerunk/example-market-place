import { Flex } from "../Vendas/styles";
import { Input } from "../Input";
import { Button } from "../Button";

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
            <Button color={"#049237"}>Adicionar</Button>
        </Flex>
        <S.Table>
            <S.Columns>
            <S.Title widthTitle="25rem">Produto/Serviço</S.Title>
            <S.Title widthTitle="15rem">Quantidade</S.Title>
            <S.Title widthTitle="15rem">Preço unitário</S.Title>
            <S.Title widthTitle="10rem">Total</S.Title>
            </S.Columns>
        </S.Table>
    </S.Container>
    </>
    )
}