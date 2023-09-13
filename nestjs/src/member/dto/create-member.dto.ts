import { IsNotEmpty, MinLength } from 'class-validator';

export class CreateMemberDto {
  @IsNotEmpty()
  @MinLength(3)
  name: string;
}
