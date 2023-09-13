import { PartialType } from '@nestjs/swagger';
import { CreateMemberDto } from './create-member.dto';
import { IsNotEmpty, MinLength } from 'class-validator';

export class UpdateMemberDto extends PartialType(CreateMemberDto) {
  @IsNotEmpty()
  @MinLength(3)
  name: string;
}
