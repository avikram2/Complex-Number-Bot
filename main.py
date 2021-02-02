import os
import math
import cmath
import re
#from discord import File
#from matplotlib import pyplot as plt
import numpy as np
from discord.ext import commands
from keep_alive import keep_alive
bot = commands.Bot(command_prefix = '$')


def numerical_check(arg1, arg2):
  try:
    arg1 = float(arg1)
    arg2 = float(arg2)
    return True
  except:
    return False

def input_verification(arg1, arg2):
  pattern = re.compile('\-?[0-9]+')
  x = re.match(pattern, arg1)
  y = re.match(pattern, arg2)
  return x and y


def multVerification(arg1, arg2, arg3, arg4):
  if (input_verification(arg1, arg2) and input_verification(arg3, arg4)):
    if numerical_check(arg1, arg2) and numerical_check(arg3, arg4):
      return True
  return False

def powVerification(arg1, arg2, arg3):
  if input_verification(arg1, arg2) and numerical_check(arg1, arg2) and numerical_check(arg3, 1):
    return True
  return False

def make_rect(r, phi):
  r = float(r)
  phi = float(phi)
  return cmath.rect(r, phi)

def make_complex(re, im):
  re = float(re)
  im = float(im)
  return complex(re, im)
def get_rect(r, phi):
  r = float(r)
  phi = float(phi)
  return cmath.rect(r, phi)
def get_polar(x):
  return cmath.polar(x)

@bot.command()
async def multRect(ctx, arg1, arg2, arg3, arg4):
  if multVerification(arg1, arg2, arg3, arg4):
    arg = [arg1, arg2, arg3, arg4]
    for x in range(len(arg)):
      arg[x] = float(arg[x])
    await ctx.send(make_complex(arg[0], arg[1])*make_complex(arg[2], arg[3]))
  else: 
    await ctx.send("Invalid")

@bot.command()
async def powerRect(ctx, arg1, arg2, arg3):
  if powVerification(arg1, arg2, arg3):
    new_list = [arg1, arg2, arg3]
    for x in range(len(new_list)):
      new_list[x] = float(new_list[x])
    await ctx.send((make_complex(new_list[0], new_list[1]))**new_list[2])
  else:
    await ctx.send("Invalid")

@bot.command()
async def multPolar(ctx, arg1, arg2, arg3, arg4):
  if multVerification(arg1, arg2, arg3, arg4):
    arg = [arg1, arg2, arg3, arg4]
    for x in range(len(arg)):
      arg[x] = float(arg[x])
    await ctx.send(make_rect(arg[0], arg[1])*make_rect(arg[2], arg[3]))
  else:
    await ctx.send("Invalid")

@bot.command()
async def powerPolar(ctx, arg1, arg2, arg3):
  if powVerification(arg1, arg2, arg3):
    new_list = [arg1, arg2, arg3]
    for x in range(len(new_list)):
      new_list[x] = float(new_list[x])
    await ctx.send("r, theta(radians): {}".format(get_polar((make_rect(new_list[0], new_list[1]))**new_list[2])))
  else:
    await ctx.send("Invalid")
@bot.command()
async def inputRectangular(ctx, arg1, arg2):
  if input_verification(arg1, arg2):
    if numerical_check(arg1, arg2):
      arg1 = float(arg1)
      arg2 = float(arg2)
      await ctx.send("Magnitude : {}".format(get_mag(arg1, arg2)))
      await ctx.send("Phase(radians) : {}".format(get_phase(arg1, arg2)))
      await ctx.send("Phase(degrees) : {}".format(np.rad2deg(get_phase(arg1, arg2))))
      await ctx.send("Polar (Radians): {}".format(get_polar(make_complex(arg1, arg2))))
    else:
      await ctx.send("Incorrect format. Send two numbers")
  else:
    await ctx.send("Incorrect format. Send two numbers")

@bot.command()
async def inputPol(ctx, arg1, arg2):
  if input_verification(arg1, arg2):
    if numerical_check(arg1, arg2):
      arg1 = float(arg1)
      arg2 = float(arg2)
      await ctx.send("Rect : {}".format(get_rect(arg1, arg2)))
    else:
      await ctx.send("Incorrect format. Send two numbers")
  else:
    await ctx.send("Incorrect format. Send two numbers")

def get_mag(re, im):
  try:
    re = float(re)
    im = float(im)
  except:
    return None
  return math.sqrt(re**2+im**2)
def get_phase(re, im):
  re = float(re)
  im = float(im)
  val = math.atan2(abs(im), abs(re))
  if (re >= 0 and im >= 0):
    return val
  elif (re < 0 and im>= 0):
    return math.pi-val
  elif (re < 0 and im < 0):
    return val-math.pi
  else: 
    return -1*val

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))
  print("Read documentation at GitHub repo Readme")

# @bot.command()
# async def graphRect(ctx, arg1, arg2):
#   pattern = re.compile('\-?[0-9]+')
#   x = re.match(pattern, arg1)
#   y = re.match(pattern, arg2)
#   if x and y:
#     try:
#       arg1 = float(arg1)
#       arg2 = float(arg2)
#     except:
#       await ctx.send("Error")
#     await ctx.send("Input is ok")
#     graph = File('graph.png')
#     ax = plt.axes()
#     ax.arrows(0, 0, arg1, arg2)
#     plt.savefig('graph.png')
#     await ctx.send(file=graph)
#   else:
#     await ctx.send("Incorrect format. Send two numbers")

keep_alive()

bot.run(os.getenv('TOKEN'))
