import { Contract } from "ethers";

export interface FL1C extends Contract {
  mint(to: string, amount: bigint): Promise<void>;
  transfer(to: string, amount: bigint): Promise<boolean>;
}
